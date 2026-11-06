#!/bin/bash
set -Eeuo pipefail

trap 'echo "❌ ERROR at line $LINENO: $BASH_COMMAND"' ERR

CONTAINER_NAME="wzmlx_container"
IMAGE_NAME="wzmlx"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "       🚀 WZMLX INSTALLER"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$EUID" -ne 0 ]; then
    echo "Please run using: sudo bash install.sh"
    exit 1
fi

cd "$(dirname "$(readlink -f "$0")")"

echo "🔧 Updating system..."
apt update
apt upgrade -y

echo "📦 Installing required packages..."
apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

echo "🧹 Cleaning old Docker repository configurations..."

grep -RIl "download.docker.com" /etc/apt/sources.list.d/ 2>/dev/null \
    | while read -r file; do
        if grep -qi "focal" "$file"; then
            echo "Removing old repository: $file"
            rm -f "$file"
        fi
    done

echo "🐳 Configuring official Docker repository..."

install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | gpg --dearmor --yes -o /etc/apt/keyrings/docker.gpg

chmod a+r /etc/apt/keyrings/docker.gpg

. /etc/os-release
CODENAME="${UBUNTU_CODENAME:-$VERSION_CODENAME}"

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu ${CODENAME} stable" \
    > /etc/apt/sources.list.d/docker.list

echo "🔄 Updating package lists..."
apt update

echo "🐳 Installing Docker..."

apt install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

echo "🚀 Starting Docker..."
systemctl enable --now docker

echo "🔍 Verifying Docker..."
docker --version
docker info

echo "🐍 Checking Python requirements..."

if [ ! -f requirements-cli.txt ]; then
    echo "❌ requirements-cli.txt not found!"
    exit 1
fi

echo "📦 Creating Python virtual environment..."

python3 -m venv .venv

echo "⬆️ Updating pip..."
.venv/bin/python -m pip install --upgrade pip setuptools wheel

echo "📦 Installing CLI dependencies..."
.venv/bin/python -m pip install -r requirements-cli.txt

echo "🏗 Building Docker image..."
docker build -t "$IMAGE_NAME" .

echo "🛑 Removing previous container..."
docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

echo "▶️ Starting Docker container..."

docker run -d \
    --name "$CONTAINER_NAME" \
    -p 80:80 \
    -p 8080:8080 \
    --restart unless-stopped \
    "$IMAGE_NAME"

echo "⏳ Waiting for container..."
sleep 5

if docker inspect -f '{{.State.Running}}' "$CONTAINER_NAME" 2>/dev/null | grep -q true; then

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "   ✅ INSTALLATION SUCCESSFUL"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    echo "🐳 Container: $CONTAINER_NAME"
    echo "🌐 Port 80: Published"
    echo "🌐 Port 8080: Published"

else

    echo ""
    echo "❌ Container failed to start!"
    echo "📋 Container logs:"
    docker logs --tail 100 "$CONTAINER_NAME" || true

    exit 1
fi

echo ""
echo "📋 Container status:"
docker ps --filter "name=^${CONTAINER_NAME}$"

echo ""
echo "✅ WZMLX deployment completed!"

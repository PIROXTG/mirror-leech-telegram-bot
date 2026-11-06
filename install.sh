set -e

echo "🔧 Updating system..."
sudo apt update -y

echo "🐍 Installing Python & pip..."
sudo apt install -y python3 python3-pip ca-certificates curl gnupg lsb-release

echo "🐳 Installing Docker (official)..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sudo sh
fi

echo "🚀 Starting Docker..."
sudo systemctl enable docker
sudo systemctl start docker

echo "📦 Installing Python CLI dependencies..."
pip3 install -r requirements-cli.txt

echo "🏗 Building Docker image..."
sudo docker build . -t wzmlx

echo "🛑 Removing old container (if any)..."
sudo docker rm -f wzmlx_container 2>/dev/null || true

echo "▶️ Running Docker container..."
sudo docker run -d \
  --name wzmlx_container \
  -p 80:80 \
  -p 8080:8080 \
  --restart unless-stopped \
  wzmlx

echo "✅ DONE! Bot is running in Docker."

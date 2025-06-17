#!/bin/bash

# CAIAC Email Template Build Script
# This script helps you get started with the React Email template

echo "🚀 CAIAC Email Template Setup"
echo "================================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed."
    echo "📦 Please install Node.js from https://nodejs.org/"
    echo ""
    echo "After installing Node.js, run:"
    echo "  npm install"
    echo "  npm run dev"
    exit 1
fi

# Check if dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

echo "✅ Setup complete!"
echo ""
echo "Available commands:"
echo "  npm run dev     - Start development server with live preview"
echo "  npm run build   - Build the email templates"
echo "  npm run export  - Export HTML files for uploading"
echo ""
echo "🌐 Run 'npm run dev' to start the development server"

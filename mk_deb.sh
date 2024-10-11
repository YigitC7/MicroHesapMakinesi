#!/bin/bash

# Değişkenler
PACKAGE_NAME="MicroHesapMakinesi"
PACKAGE_VERSION="1.0"
PACKAGE_DIR="$PACKAGE_NAME-$PACKAGE_VERSION"

# Paket dizinlerini oluştur
mkdir -p "$PACKAGE_DIR/DEBIAN"
mkdir -p "$PACKAGE_DIR/usr/local/bin"
mkdir -p "$PACKAGE_DIR/usr/share/icons"
mkdir -p "$PACKAGE_DIR/usr/local/share/applications"

# Kontrol dosyasını oluştur (boş)
cat << EOF > "$PACKAGE_DIR/DEBIAN/control"
Package: $PACKAGE_NAME
Version: $PACKAGE_VERSION
Section: utils
Priority: optional
Architecture: amd64
Depends: 
Maintainer: Yigit <yigitcitak.1817@gmail.com>
Description: Micro Hesap Makinesi programı
EOF

# Masaüstü dosyasını oluştur (boş)
cat << EOF > "$PACKAGE_DIR/usr/local/share/applications/$PACKAGE_NAME.desktop"
[Desktop Entry]
Version=1.0
Type=Application
Name=Micro Hesap Makinesi
Exec=/usr/local/bin/microHesap/Main
Icon=/usr/local/bin/microHesap/icon.png
Terminal=false
Categories=Utility;Application;
EOF

# Dosyaları yerleştirme
cp -r dist/Main $PACKAGE_DIR/usr/local/bin/microHesap
cp -f img/icon.png $PACKAGE_DIR/usr/local/bin/microHesap/icon.png

# Deb yapmak
dpkg-deb --build $PACKAGE_DIR

echo "Dizin yapısı oluşturuldu: $PACKAGE_DIR"
echo "Micropad deb paketi oluşturuldu"


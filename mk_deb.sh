#!/bin/bash

# Değişkenler
PACKAGE_NAME="microhesapmakinesi"
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
Description: Micro hesap makinesi programı
EOF

# Masaüstü dosyasını oluştur (boş)
cat << EOF > "$PACKAGE_DIR/usr/local/share/applications/$PACKAGE_NAME.desktop"
[Desktop Entry]
Version=1.0
Type=Application
Name=Micro Hesap Makinesi
Exec=/usr/local/bin/micro_hesap_makinesi/Main
Icon=/usr/local/bin/micro_hesap_makinesi/icon.png
Terminal=false
Categories=Utility;Application;
EOF

cp -r dist/Main $PACKAGE_DIR/usr/local/bin/micro_hesap_makinesi
cp -f img/icon.png $PACKAGE_DIR/usr/local/bin/micro_hesap_makinesi/icon.png

dpkg-deb --build $PACKAGE_DIR

echo "Dizin yapısı oluşturuldu: $PACKAGE_DIR"



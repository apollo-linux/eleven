build_dir := env("BUILD_DIR", "_build")
install_prefix := env("INSTALL_PREFIX", "/usr/local/")
just := just_executable()

alias setup := setup-builddir

[private]
default:
    {{ just }} install
    eleven

update_potfiles:
    #!/usr/bin/env bash

    BUILD_DIR="translation-build/"
    if [ -d "$BUILD_DIR" ]; then
        rm -r translation-build
    fi

    meson translation-build
    meson compile -C translation-build eleven-pot
    meson compile -C translation-build eleven-update-po

    rm -r translation-build

setup-builddir:
    #!/usr/bin/env bash

    meson setup --wipe {{build_dir}} --prefix {{install_prefix}}

install: 
    #!/usr/bin/env bash

    cd {{build_dir}}
    sudo meson install
    cd ..

# Install dependencies on Arch
install-arch-deps:
    #!/usr/bin/env bash

    sudo pacman -S \
        meson \
        ninja \
        gtk4 \
        git \
        appstream \
        python-gobject \
        libadwaita
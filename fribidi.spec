#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : fribidi
Version  : 1.0.10
Release  : 21
URL      : file:///insilications/build/clearlinux/packages/fribidi/fribidi-v1.0.10.zip
Source0  : file:///insilications/build/clearlinux/packages/fribidi/fribidi-v1.0.10.zip
Summary  : Unicode Bidirectional Algorithm Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: fribidi-bin = %{version}-%{release}
Requires: fribidi-lib = %{version}-%{release}
BuildRequires : binutils
BuildRequires : binutils-dev
BuildRequires : buildreq-meson
BuildRequires : findutils
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package bin
Summary: bin components for the fribidi package.
Group: Binaries

%description bin
bin components for the fribidi package.


%package dev
Summary: dev components for the fribidi package.
Group: Development
Requires: fribidi-lib = %{version}-%{release}
Requires: fribidi-bin = %{version}-%{release}
Provides: fribidi-devel = %{version}-%{release}
Requires: fribidi = %{version}-%{release}

%description dev
dev components for the fribidi package.


%package dev32
Summary: dev32 components for the fribidi package.
Group: Default
Requires: fribidi-lib32 = %{version}-%{release}
Requires: fribidi-bin = %{version}-%{release}
Requires: fribidi-dev = %{version}-%{release}

%description dev32
dev32 components for the fribidi package.


%package lib
Summary: lib components for the fribidi package.
Group: Libraries

%description lib
lib components for the fribidi package.


%package lib32
Summary: lib32 components for the fribidi package.
Group: Default

%description lib32
lib32 components for the fribidi package.


%package staticdev
Summary: staticdev components for the fribidi package.
Group: Default
Requires: fribidi-dev = %{version}-%{release}

%description staticdev
staticdev components for the fribidi package.


%package staticdev32
Summary: staticdev32 components for the fribidi package.
Group: Default
Requires: fribidi-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the fribidi package.


%prep
%setup -q -n fribidi-v1.0.10
cd %{_builddir}/fribidi-v1.0.10
pushd ..
cp -a fribidi-v1.0.10 build32
popd

%build
## build_prepend content
#find . -type f -name 'git.mk' -exec rm {} \;
#find . -type f -name 'configure.ac' -exec sed -i '/doc\/Makefile/d' {} \;
#find . -type d -name 'doc' -exec rm -rf {} 2> /dev/null \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596933636
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto=16 $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto=16 $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto=16 $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -flto=16 $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -flto=16 $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto=16 $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto=16 $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto=16 $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -flto=16 $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -flto=16 $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen --enable-shared --enable-static --disable-docs
make  V=1 VERBOSE=1

make -j16 VERBOSE=1 V=1 check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen  --enable-shared --enable-static --disable-docs
make  V=1 VERBOSE=1

pushd ../build32/
## build_prepend content
#find . -type f -name 'git.mk' -exec rm {} \;
#find . -type f -name 'configure.ac' -exec sed -i '/doc\/Makefile/d' {} \;
#find . -type d -name 'doc' -exec rm -rf {} 2> /dev/null \;
## build_prepend end
export CFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O3 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen  --enable-shared --enable-static --disable-docs  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make check
cd ../build32;
make check || :

%install
export SOURCE_DATE_EPOCH=1596933636
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fribidi

%files dev
%defattr(-,root,root,-)
/usr/include/fribidi/fribidi-arabic.h
/usr/include/fribidi/fribidi-begindecls.h
/usr/include/fribidi/fribidi-bidi-types-list.h
/usr/include/fribidi/fribidi-bidi-types.h
/usr/include/fribidi/fribidi-bidi.h
/usr/include/fribidi/fribidi-brackets.h
/usr/include/fribidi/fribidi-char-sets-list.h
/usr/include/fribidi/fribidi-char-sets.h
/usr/include/fribidi/fribidi-common.h
/usr/include/fribidi/fribidi-config.h
/usr/include/fribidi/fribidi-deprecated.h
/usr/include/fribidi/fribidi-enddecls.h
/usr/include/fribidi/fribidi-flags.h
/usr/include/fribidi/fribidi-joining-types-list.h
/usr/include/fribidi/fribidi-joining-types.h
/usr/include/fribidi/fribidi-joining.h
/usr/include/fribidi/fribidi-mirroring.h
/usr/include/fribidi/fribidi-shape.h
/usr/include/fribidi/fribidi-types.h
/usr/include/fribidi/fribidi-unicode-version.h
/usr/include/fribidi/fribidi-unicode.h
/usr/include/fribidi/fribidi.h
/usr/lib64/libfribidi.so
/usr/lib64/pkgconfig/fribidi.pc
/usr/share/man/man3/fribidi_charset_to_unicode.3
/usr/share/man/man3/fribidi_debug_status.3
/usr/share/man/man3/fribidi_get_bidi_type.3
/usr/share/man/man3/fribidi_get_bidi_type_name.3
/usr/share/man/man3/fribidi_get_bidi_types.3
/usr/share/man/man3/fribidi_get_bracket.3
/usr/share/man/man3/fribidi_get_bracket_types.3
/usr/share/man/man3/fribidi_get_joining_type.3
/usr/share/man/man3/fribidi_get_joining_type_name.3
/usr/share/man/man3/fribidi_get_joining_types.3
/usr/share/man/man3/fribidi_get_mirror_char.3
/usr/share/man/man3/fribidi_get_par_direction.3
/usr/share/man/man3/fribidi_get_par_embedding_levels.3
/usr/share/man/man3/fribidi_get_par_embedding_levels_ex.3
/usr/share/man/man3/fribidi_get_type.3
/usr/share/man/man3/fribidi_get_type_internal.3
/usr/share/man/man3/fribidi_join_arabic.3
/usr/share/man/man3/fribidi_log2vis.3
/usr/share/man/man3/fribidi_log2vis_get_embedding_levels.3
/usr/share/man/man3/fribidi_mirroring_status.3
/usr/share/man/man3/fribidi_parse_charset.3
/usr/share/man/man3/fribidi_remove_bidi_marks.3
/usr/share/man/man3/fribidi_reorder_line.3
/usr/share/man/man3/fribidi_reorder_nsm_status.3
/usr/share/man/man3/fribidi_set_debug.3
/usr/share/man/man3/fribidi_set_mirroring.3
/usr/share/man/man3/fribidi_set_reorder_nsm.3
/usr/share/man/man3/fribidi_shape.3
/usr/share/man/man3/fribidi_shape_arabic.3
/usr/share/man/man3/fribidi_shape_mirroring.3
/usr/share/man/man3/fribidi_unicode_to_charset.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfribidi.so
/usr/lib32/pkgconfig/32fribidi.pc
/usr/lib32/pkgconfig/fribidi.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfribidi.so.0
/usr/lib64/libfribidi.so.0.4.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfribidi.so.0
/usr/lib32/libfribidi.so.0.4.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libfribidi.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libfribidi.a

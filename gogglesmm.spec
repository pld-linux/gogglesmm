Summary:	Goggles Music Manager - a music collection manager and player
Summary(hu.UTF-8):	Goggles Music Manager egy zenegyűjtemény-kezelő és lejátszó
Summary(pl.UTF-8):	Goggles Music Manager - zarządca i odtwarzacz kolekcji muzyki
Name:		gogglesmm
Version:	1.3.1
Release:	3
License:	GPL v3+
Group:		X11/Applications/Multimedia
Source0:	https://github.com/gogglesmm/gogglesmm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	52e7af720aed7835a3be6b1b824eba4b
URL:		https://github.com/gogglesmm/gogglesmm
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 3.23
BuildRequires:	dbus-devel
BuildRequires:	expat-devel
BuildRequires:	faad2-devel >= 2
BuildRequires:	flac-devel
BuildRequires:	fox-devel >= 1.7.19-6
BuildRequires:	gettext-tools
BuildRequires:	libdts-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libstdc++-devel >= 6:4.7
# or gnutls with -DWITH_OPENSSL=OFF, or libgcrypt with -DWITH_OPENSSL=OFF -DWITH_GNUTLS=OFF
BuildRequires:	openssl-devel >= 1.0.1
BuildRequires:	opus-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel >= 3.6.19
BuildRequires:	taglib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	sqlite3%{?_isa} >= 3.6.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Goggles Music Manager is a music collection manager and player that
automatically categorizes your music files based on genre, artist,
album, and song. It supports gapless playback and features easy tag
editing.

%description -l hu.UTF-8
Goggles Music Manager egy zenegyűjtemény kezelő és lejátszó, amely
automatikusan kategorizálja a zenefájlaidat stítlus, előadó, album és
dal alapján. Szünetmentes lejátszást és könnyű tag-szerkesztést is
biztosít.

%description -l pl.UTF-8
Goggles Music Manager to zarządca i odtwarzacz kolekcji muzyki,
automatycznie kategoryzujący pliki muzyczne w oparciu o gatunek,
artystę, album i utwór. Obsługuje odtwarzanie bez przerw, umożliwia
łatwe modyfikowanie znaczników.

%package devel
Summary:	Header files for gap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gap
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for gap (Goggles Audio Player) library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gap (Goggles Audio Player).

%prep
%setup -q

%build
%cmake -B build \
	-DFOX_USE_EXTERNAL=ON \
	-DWITH_A52=ON \
	-DWITH_DCA=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/gogglesmm
%{_libdir}/libgap.so.*.*.*
%ghost %{_libdir}/libgap.so.0
%dir %{_libdir}/gogglesmm
%{_libdir}/gogglesmm/libgap_alsa.so
%{_libdir}/gogglesmm/libgap_pulse.so
%{_libdir}/gogglesmm/libgap_wav.so
%{_datadir}/metainfo/gogglesmm.appdata.xml
%{_mandir}/man1/gogglesmm.1*
%{_desktopdir}/gogglesmm.desktop
%{_iconsdir}/hicolor/*x*/apps/gogglesmm.png
%{_iconsdir}/hicolor/scalable/apps/gogglesmm.svg

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgap.so
%{_includedir}/gap
%{_libdir}/cmake/gap


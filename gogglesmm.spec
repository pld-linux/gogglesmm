Summary:	Goggles Music Manager is a music collection manager and player
Summary(hu.UTF-8):	Goggles Music Manager egy zenegyűjtemény-kezelő és lejátszó
Name:		gogglesmm
Version:	1.3.1
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	https://github.com/gogglesmm/gogglesmm/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	52e7af720aed7835a3be6b1b824eba4b
URL:		https://github.com/gogglesmm/gogglesmm
BuildRequires:	bash
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	fox-devel >= 1.7.19-6
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	taglib-devel
BuildRequires:	taglib-extras-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xine-lib-devel
Requires:	xine-plugin-audio
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

%package devel
Summary:	Header files for gap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gap.

%prep
%setup -q

%build
mkdir -p build
cd build
%cmake ../ \
	-DFOX_USE_EXTERNAL=ON

%{__make}

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
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/gogglesmm/libgap_alsa.so
%{_libdir}/gogglesmm/libgap_pulse.so
%{_libdir}/gogglesmm/libgap_wav.so
%{_libdir}/libgap.so.*.*.*
%ghost %{_libdir}/libgap.so.0
%{_mandir}/man1/%{name}*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/gogglesmm.appdata.xml

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgap.so
%{_includedir}/gap
%{_libdir}/cmake/gap


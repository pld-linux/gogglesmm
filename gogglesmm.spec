Summary:	Goggles Music Manager is a music collection manager and player
Summary(hu.UTF-8):	Goggles Music Manager egy zenegyűjtemény-kezelő és lejátszó
Name:		gogglesmm
Version:	0.12.7
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://gogglesmm.googlecode.com/files/%{name}-%{version}.tar.xz
# Source0-md5:	c59f004806bdee8cd8c9353729c82262
Patch0:		fox.patch
URL:		http://code.google.com/p/gogglesmm/
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

%prep
%setup -q
%patch0 -p1
#for verbose build
sed 's/^\t@/\t/' -i Makefile

%build
CFLAGS="%{rpmcxxflags}" \
INCFLAGS="%{rpmcppflags} $(pkg-config --cflags-only-I fox17 taglib dbus-1)" \
CXX="%{__cxx}" \
LINK="%{__cxx}" \
LDFLAGS="%{rpmcxxflags} %{rpmldflags}" \
LIBPREFIX="%{_libdir}" \
PKG_PREFIX="%{_prefix}" \
./configure --with-fox17

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

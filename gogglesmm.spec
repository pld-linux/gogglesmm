Summary:	Goggles Music Manager is a music collection manager and player
Summary(hu.UTF-8):	Goggles Music Manager egy zenegyűjtemény-kezelő és lejátszó
Name:		gogglesmm
Version:	0.10.27
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	http://gogglesmm.googlecode.com/files/%{name}-%{version}.tar.xz
# Source0-md5:	5e989de4ee33d870acef6bc3cf9449f8
URL:		http://code.google.com/p/gogglesmm/
BuildRequires:	bash
BuildRequires:	dbus-devel
BuildRequires:	fox-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	taglib-devel
BuildRequires:	taglib-extras-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xine-lib-devel
Requires:	xine-plugin-audio
Suggests:	libfetch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Goggles Music Manager is a music collection manager and player that
automatically categorizes your music files based on genre, artist,
album, and song. It supports gapless playback and features easy tag
editing.

%description -l hu.UTF-8
Goggles Musinc Manager egy zenegyűjtemény kezelő és lejátszó, amely
automatikusan kategorizálja a zenefájlaidat stítlus, előadó, album és
dal alapján. Szünetmentes lejátszást és könnyű tag-szerkesztést is
biztosít.

%prep
%setup -q
#for verbose build
sed 's/^\t@/\t/' -i Makefile

%build
CFLAGS="%{rpmcxxflags}" \
INCFLAGS="%{rpmcppflags}" \
CXX="%{__cxx}" \
LINK="%{__cxx}" \
LDFLAGS="%{rpmcxxflags} %{rpmldflags}" \
LIBPREFIX="%{_libdir}" \
./configure

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
%{_iconsdir}/hicolor/48x48/apps/%{name}.png

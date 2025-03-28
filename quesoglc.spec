Summary:	QuesoGLC - free implementation of the OpenGL Character Renderer (GLC)
Summary(pl.UTF-8):	QuesoGLC - wolnodostępna implementacja "OpenGL Character Renderer" (GLC)
Name:		quesoglc
Version:	0.7.2
Release:	5
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/quesoglc/%{name}-%{version}.tar.bz2
# Source0-md5:	1c8d394d4f41fa0c5b08eb7ead73c4ef
Patch0:		%{name}-types.patch
URL:		https://quesoglc.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	fontconfig-devel >= 1:2.2
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%description -l pl.UTF-8
QuesoGLC to wolnodostępna implementacja "OpenGL Character Renderer"
(GLC). Jest oparta na bibliotece FreeType, zapewnia obsługę Unikodu i
jest zaprojektowana jako przenośna na dowolną platformę obsługującą
FreeType i API OpenGL.

%package devel
Summary:	Header files QuesoGLC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QuesoGLC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	fontconfig-devel >= 1:2.2
Requires:	freetype-devel >= 2.1.0

%description devel
This package includes the header files for QuesoGLC library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki QuesoGLC.

%package static
Summary:	Static QuesoGLC library
Summary(pl.UTF-8):	Statyczna biblioteka QuesoGLC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static QuesoGLC library.

%description static -l pl.UTF-8
Statyczna biblioteka QuesoGLC.

%prep
%setup -q
%patch -P0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libGLC.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/libGLC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLC.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLC.so
%{_includedir}/GL/glc.h
%{_pkgconfigdir}/quesoglc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libGLC.a

# TODO: 
# - static package?
#
# Conditional build:
#
Summary:	QuesoGLC is a free (as in free speech) implementation of the OpenGL Character Renderer (GLC)
Summary(pl.UTF-8):	QuesoGLC to wolna implementacja "OpenGL Character Renderer" (GLC)
Name:		quesoglc
Version:	0.6.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/quesoglc/%{name}-%{version}.tar.bz2
# Source0-md5:	7fbdc3b57a179a471a8ca2e590a2f56b
URL:		http://quesoglc.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:  freetype-devel >= 2.0.0
BuildRequires:	fontconfig-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuesoGLC is a free (as in free speech) implementation of the OpenGL
Character Renderer (GLC). QuesoGLC is based on the FreeType library,
provides Unicode support and is designed to be easily ported to any
platform that supports both FreeType and the OpenGL API.

%description -l pl.UTF-8
QuesoGLC to wolna implementacja "OpenGL Character Renderer" (GLC).
QuesoGLC bazuje na bibliotece FreeType. Oferuje wsparcie dla Unikodu i
zbudowany jest po to aby był łatwo przenoszony na dowolną
platformę, która wspiera FreeType i API OpenGL.

%package devel
Summary:	Header files QuesoGLC library
Summary(pl.UTF-8):Pliki nagłówkowe biblioteki QuesoGLC
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the header files for QuesoGLC library.

%description devel -l pl.UTF-8
Ta paczka zawiera pliki nagłówkowe biblioteki QuesoGLC.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/libGLC.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog README THANKS
%attr(755,root,root) %{_libdir}/libGLC*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/GL/*.h
%{_libdir}/libGLC*.la

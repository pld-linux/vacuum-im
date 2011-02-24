%define		sname	vacuum
Summary:	Crossplatform Jabber client written on Qt
Summary(pl.UTF-8):	Międzyplatformowy klient Jabbera napisany w Qt
Name:		vacuum-im
Version:	1.0.2
Release:	1
License:	GPL v3+
Group:		Applications/Communications
Source0:	http://vacuum-im.googlecode.com/files/%{sname}-%{version}-source.tar.gz
# Source0-md5:	96f6a1510f9a9a94e0a90fc060924fa0
Patch0:		%{name}-qHash.patch
Patch1:		%{name}-desktop.patch
URL:		http://code.google.com/p/vacuum-im/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The core program is just a plugin loader - all functionality is made
available via plugins. This enforces modularity and ensures well
defined component interaction via interfaces.

%description -l pl.UTF-8
Główny program służy tylko do ładowania wtyczek - cała funkcjonalność
opiera się na wtyczkach. Umożliwia to modularność oraz poprawne
definiowanie interakcji komponentów poprzez interfejsy.

%package devel
Summary:	Development files for Vacuum-IM
Summary(pl.UTF-8):	Pliki deweloperskie dla Vacuum-IM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package includes files needed to develop Vacuum-IM modules.

%description devel -l pl.UTF-8
Ta paczka zawiera pliki niezbędne do rozwijania modułów dla Vacuum-IM.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p1
%patch1 -p1

%build
qmake-qt4 -recursive vacuum.pro \
	INSTALL_PREFIX="%{_prefix}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# vacuum -> vacuum-im to avoid conflicts with vacuum.spec
mv $RPM_BUILD_ROOT%{_bindir}/%{sname} $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_desktopdir}/%{sname}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
mv $RPM_BUILD_ROOT%{_pixmapsdir}/%{sname}.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libvacuumutils.so.*.*.*
%attr(755,root,root) %{_libdir}/libvacuumutils.so.1
%attr(755,root,root) %ghost %{_libdir}/libvacuumutils.so.1.0
%dir %{_libdir}/%{sname}
%dir %{_libdir}/%{sname}/plugins
%attr(755,root,root) %{_libdir}/%{sname}/plugins/*.so
%dir %{_datadir}/%{sname}
%dir %{_datadir}/%{sname}/resources
%{_datadir}/%{sname}/resources/*
%dir %{_datadir}/%{sname}/translations
%{_datadir}/%{sname}/translations/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%files devel
%defattr(644,root,root,755)
%{_libdir}/libvacuumutils.so

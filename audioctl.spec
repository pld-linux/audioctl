Summary:	Utility to control sparc audio device
Summary(pl.UTF-8):	Narzędzie do sterowania urządzeniem dźwiękowym w sparcach
Name:		audioctl
Version:	1.3
Release:	1
License:	BSD
Group:		Applications/Sound
Source0:	ftp://ftp.dementia.org/pub/linux/sparc/audio/%{name}-%{version}.tar.gz
# Source0-md5:	320e8cf844fb26720c256a04ae221cc6
Requires:	dev >= 2.9.0-10
ExclusiveArch:	sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The audioctl command displays or sets various audio system driver
variables. It is NetBSD utility ported to sparc-linux.

%description -l pl.UTF-8
Polecenie audioctl wyświetla i ustawia różne parametry dotyczące
systemowego sterownika dźwięku. Jest to port narzędzia z NetBSD na
architekturę sparc-linux.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install audioctl $RPM_BUILD_ROOT%{_bindir}
install audioctl.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/audioctl
%{_mandir}/man1/audioctl.1*

Summary:	Userspace support for digital cameras
Summary(pl.UTF-8):	Wsparcie dla kamer cyfrowych w przestrzeni użytkownika
Name:		hal-gphoto
# XXX: update versioning to follow gphoto2 version which data supports?
Version:	0.5.9
Release:	2
# ?
License:	GPL v2
Group:		Applications/System
Source0:	hal-libgphoto2.fdi
Source1:	hal-libgphoto_udev.rules
Requires:	hal >= 0.5.9-2
Requires:	libusb >= 0.1.10a
Requires:	udev >= 1:089
Provides:	udev-digicam
Obsoletes:	hotplug-digicam
Obsoletes:	udev-digicam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of Udev rules and HAL device information file to handle digital
cameras in userspace.

%description -l pl.UTF-8
Zestaw reguł Udev i plik z informacjami o urządzeniach HAL-a do
obsługi kamer cyfrowych w przestrzeni użytkownika.

%prep

%install
install -d $RPM_BUILD_ROOT{%{_datadir}/hal/fdi/information,%{_sysconfdir}/udev/rules.d}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}/fdi/information/10freedesktop/10-gphoto.fdi
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/52-udev-gphoto.rules

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q haldaemon restart
%banner %{name} -e << EOF
WARNING!
 hal-gphoto NO LONGER uses special "digicam" group.
 Please add yourself to more common "usb" group instead.

EOF

%files
%defattr(644,root,root,755)
%{_sysconfdir}/udev/rules.d/52-udev-gphoto.rules
%{_datadir}/%{name}/fdi/information/10freedesktop/10-gphoto.fdi

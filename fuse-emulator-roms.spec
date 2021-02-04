Name:           fuse-emulator-roms
Epoch:		1
Version:        0.9.0
Release:        15%{?dist}
Summary:        Spectrum ROM files for use with the Fuse emulator
Group:          Applications/Emulators
License:        Distributable
URL:            http://fuse-emulator.sourceforge.net
Source0:        http://downloads.sourceforge.net/fuse-emulator/fuse-%{version}.tar.gz
Source1:        rom-distribution.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  desktop-file-utils
Requires:       fuse-emulator
Provides:	%{name} = 2:0.9.0-2
Obsoletes:	%{name} = 1.2-1

%description
The Spectrum ROM files, for use with the Fuse Emulator.


%prep
%setup -q -n fuse-%{version}


%build
# Build desktop icon
cat >fuse-emulator.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Fuse
GenericName=(Spectrum Emulator)
Comment=Emulates various models of spectrums and clones
Exec=fuse
Icon=fuse-emulator.png
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/fuse
install -pm 0644 roms/*.rom %{buildroot}%{_datadir}/fuse
install -pm 0644 %{SOURCE1} %{_builddir}/fuse-%{version}/rom-distribution.txt

desktop-file-install \
                     --dir %{buildroot}%{_datadir}/applications \
                     fuse-emulator.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/fuse/*.rom
%{_datadir}/applications/fuse-emulator.desktop
%doc rom-distribution.txt


%changelog
* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:0.9.0-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1:0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1:0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:0.9.0-5
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1:0.9.0-3
- rebuild for new F11 features

* Wed Aug 13 2008 Lucian Langa <cooly@gnome.eu.org> - 1:0.9.0-2
- Fix EVR issues

* Mon Jul 28 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.0-1
- Make version match fuse-emulator
- Initial rpmfusion import

* Sat Jul 07 2007 Ian Chapman <packages@amiga-hardware.com> - 1.1-1
- Updated rom set to those included with fuse 0.8.0.1

* Sun Mar 04 2007 Ian Chapman <packages@amiga-hardware.com> - 1.0-2
- Changed .desktop categories to Game;Emulator;
- Updated source URL in comment

* Sun Aug 06 2006 Ian Chapman <packages@amiga-hardware.com> - 1.0-1
- Initial release

%define distsuffix edm

Summary:        Take Gimp work on one window interface
Name:           gimpbox
Version:        0.1.0
Release:        4
License:        GPLv2+
Group:          Graphics
Source0:        http://gimpbox.googlecode.com/hg/%{name}.py
BuildArch:      noarch
Requires:	gimp >= 2.6.10
Requires:	gnome-python-desktop
Requires:	libwnck

%description
gimbox is a small script on python, running Gimp on one window interface

%prep

%build

%install

mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp %SOURCE0  ${RPM_BUILD_ROOT}/%{_bindir}/%{name}

%clean

%post

rm -f /usr/bin/gimp
ln -s /usr/bin/%{name} /usr/bin/gimp
sed -i '/Exec/s/gimp-2.6/gimpbox/g' /usr/share/applications/gimp.desktop

%postun

rm -f /usr/bin/gimp
ln -s /usr/bin/gimp-2.6 /usr/bin/gimp
sed -i '/Exec/s/gimpbox/gimp-2.6/g' /usr/share/applications/gimp.desktop


%files
%defattr(-, root, root, -)

%{_bindir}/gimpbox



%changelog
* Fri May 06 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.0-2edm2011.0
+ Revision: 670802
- imported package gimpbox

* Tue Dec 28 2010 Александр Казанцев <kazancas@mandriva.org> 0.1.0-1mdv2011.0
+ Revision: 625508
- import gimpbox


* Tue Nov 9 2010 Alexander Kazancev <kazancas@mandriva.ru> - 0.1.0
- initial build



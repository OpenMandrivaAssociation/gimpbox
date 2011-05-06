%define distsuffix edm

Summary:        Gimpbox take Gimp work on one window interface
Name:           gimpbox
Version:        0.1.0
Release:        %mkrel 1
License:        GPLv2+
Group:          System Environment/Base
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
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}/%{_bindir}
cp %SOURCE0  ${RPM_BUILD_ROOT}/%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

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


%{?!module_name: %{error: You did not specify a module name (%%module_name)}}
%{?!version: %{error: You did not specify a module version (%%version)}}
%{?!kernel_versions: %{error: You did not specify kernel versions (%%kernel_version)}}
%{?!packager: %define packager DKMS <dkms-devel@lists.us.dell.com>}
%{?!license: %define license Unknown}
%{?!_dkmsdir: %define _dkmsdir /var/lib/dkms}
%{?!_srcdir: %define _srcdir %_prefix/src}
%{?!_datarootdir: %define _datarootdir %{_datadir}}

Summary:	%{module_name} %{version} dkms package
Name:		%{module_name}
Version:	%{version}
License:	%license
Release:	1dkms
BuildArch:	noarch
Group:		System/Kernel
Requires: 	dkms >= 1.95
Requires: 	coreutils
Requires: 	grep
Requires: 	sed
BuildRequires: 	dkms
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root/

%description
Kernel modules for %{module_name} %{version} in a DKMS wrapper.

%prep
if [ "%mktarball_line" != "none" ]; then
        /usr/sbin/dkms mktarball -m %module_name -v %version %mktarball_line --archive `basename %{module_name}-%{version}.dkms.tar.gz`
        cp -af %{_dkmsdir}/%{module_name}/%{version}/tarball/`basename %{module_name}-%{version}.dkms.tar.gz` %{module_name}-%{version}.dkms.tar.gz
fi

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
        rm -rf $RPM_BUILD_ROOT
fi
mkdir -p $RPM_BUILD_ROOT/%{_srcdir}
mkdir -p $RPM_BUILD_ROOT/%{_datarootdir}/%{module_name}

if [ -d %{_sourcedir}/%{module_name}-%{version} ]; then
        cp -Lpr %{_sourcedir}/%{module_name}-%{version} $RPM_BUILD_ROOT/%{_srcdir}
fi

if [ -f %{module_name}-%{version}.dkms.tar.gz ]; then
        install -m 644 %{module_name}-%{version}.dkms.tar.gz $RPM_BUILD_ROOT/%{_datarootdir}/%{module_name}
fi

if [ -f %{_sourcedir}/common.postinst ]; then
        install -m 755 %{_sourcedir}/common.postinst $RPM_BUILD_ROOT/%{_datarootdir}/%{module_name}/postinst
fi

# install udev rules and required scripts
mkdir -p $RPM_BUILD_ROOT/etc/udev/rules.d
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/lib/udev
install -m 644 $RPM_BUILD_ROOT/%{_srcdir}/%{name}-%{version}/dkms/target_files/99-spar_guest.rules        $RPM_BUILD_ROOT/etc/udev/rules.d/99-spar_guest.rules
install -m 755 $RPM_BUILD_ROOT/%{_srcdir}/%{name}-%{version}/dkms/target_files/spar_parahotplug.sh        $RPM_BUILD_ROOT/sbin/spar_parahotplug.sh
install -m 755 $RPM_BUILD_ROOT/%{_srcdir}/%{name}-%{version}/dkms/target_files/spar_visorchipset_guest.sh $RPM_BUILD_ROOT/lib/udev/spar_visorchipset_guest.sh

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
        rm -rf $RPM_BUILD_ROOT
fi

%post
for POSTINST in %{_libdir}/dkms/common.postinst %{_datarootdir}/%{module_name}/postinst; do
        if [ -f $POSTINST ]; then
                $POSTINST %{module_name} %{version} %{_datarootdir}/%{module_name}
                exit $?
        fi
        echo "WARNING: $POSTINST does not exist."
done
echo -e "ERROR: DKMS version is too old and %{module_name} was not"
echo -e "built with legacy DKMS support."
echo -e "You must either rebuild %{module_name} with legacy postinst"
echo -e "support or upgrade DKMS to a more current version."
exit 1

%preun
echo -e
echo -e "Uninstall of %{module_name} module (version %{version}) beginning:"
dkms remove -m %{module_name} -v %{version} --all --rpm_safe_upgrade
exit 0

%files
%defattr(-,root,root)
%{_srcdir}
%{_datarootdir}/%{module_name}/
/etc/udev/rules.d/99-spar_guest.rules
/sbin/spar_parahotplug.sh
/lib/udev/spar_visorchipset_guest.sh

%changelog
* %(date "+%a %b %d %Y") %packager %{version}-%{release}
- Automatic build by DKMS


# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       intltool
Summary:    Utility for internationalizing various kinds of data files
Version:    0.50.1
Release:    1
Group:      Development/Tools
License:    GPLv2 with exceptions
URL:        http://freedesktop.org/wiki/Software/intltool
Source0:    http://launchpad.net/intltool/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source100:  intltool.yaml
Requires:   patch
Requires:   automake
Requires:   gettext-devel
Requires:   perl(XML::Parser)
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext


%description
This tool automatically extracts translatable strings from oaf, glade,
bonobo ui, nautilus theme, .desktop, and other data files and puts
them in the po files.




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README
%doc %{_mandir}/man*/*
%{_bindir}/*
%{_datadir}/intltool
%{_datadir}/aclocal/*
# << files



# Generated from rexical-1.0.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rexical
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Rexical is a lexical scanner generator
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.0.4
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/tenderlove/rexical/tree/master
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(hoe) >= 2.3.1
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Rexical is a lexical scanner generator.
It is written in Ruby itself, and generates Ruby program.
It is designed for use with Racc.

%prep

if ! [ -e %{ruby} ]; then
    echo "Please provide your ruby enterprise path"
    echo "%{ruby} does not exists"
    echo "Use: --define 'ruby ruby path'"
    exit 1
fi

rubyrpm=`rpm -q --whatprovides %{ruby}`

if ! [[ $rubyrpm =~ ^ruby-enterprise ]]; then
    echo "Please provide your ruby enterprise path"
    echo "%{ruby} it's not from the ruby-enterprise RPM"
    echo "Use: --define 'ruby ruby path'"
    exit 1
fi

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/rex
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/DOCUMENTATION.en.rdoc
%doc %{geminstdir}/DOCUMENTATION.ja.rdoc
%doc %{geminstdir}/README.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Sat Nov 13 2010 Roberto Gaiser <rgaiser@shrek.intranet> - 1.0.4-1
- Initial package

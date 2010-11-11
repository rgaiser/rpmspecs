# Generated from passenger-3.0.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby /usr/local/bin/ruby
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname passenger
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Easy and robust Ruby web application deployment
Name: ruby-enterprise-rubygem-%{gemname}
Version: 3.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.modrails.com/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(rake) >= 0.8.1
Requires: ruby-enterprise-rubygem(fastthread) >= 1.0.1
Requires: ruby-enterprise-rubygem(daemon_controller) >= 0.2.5
Requires: ruby-enterprise-rubygem(file-tail) >= 0
Requires: ruby-enterprise-rubygem(rack) >= 0
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Easy and robust Ruby web application deployment.


%prep

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
%{_bindir}/passenger
%{_bindir}/passenger-install-apache2-module
%{_bindir}/passenger-install-nginx-module
%{_bindir}/passenger-config
%{_bindir}/passenger-stress-test
%{_bindir}/passenger-status
%{_bindir}/passenger-memory-stats
%{_bindir}/passenger-make-enterprisey
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 3.0.0-1
- Initial package

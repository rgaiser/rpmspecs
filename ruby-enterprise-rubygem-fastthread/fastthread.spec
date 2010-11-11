# Generated from fastthread-1.0.7.gem by gem2rpm -*- rpm-spec -*-
%define ruby /usr/local/bin/ruby
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname fastthread
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Optimized replacement for thread.rb primitives
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.0.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/fauna/mongrel
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Optimized replacement for thread.rb primitives


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/ext/fastthread/fastthread.c
%doc %{geminstdir}/ext/fastthread/extconf.rb
%doc %{geminstdir}/CHANGELOG
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 1.0.7-1
- Initial package

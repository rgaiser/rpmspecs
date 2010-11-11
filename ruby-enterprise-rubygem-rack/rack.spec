# Generated from rack-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby /usr/local/bin/ruby
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rack
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a modular Ruby webserver interface
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.2.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rack.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(bacon) >= 0
Requires: ruby-enterprise-rubygem(rake) >= 0
Requires: ruby-enterprise-rubygem(fcgi) >= 0
Requires: ruby-enterprise-rubygem(memcache-client) >= 0
Requires: ruby-enterprise-rubygem(mongrel) >= 0
Requires: ruby-enterprise-rubygem(thin) >= 0
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.rubyforge.org.


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
%{_bindir}/rackup
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/SPEC
%doc %{geminstdir}/KNOWN-ISSUES
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 1.2.1-1
- Initial package

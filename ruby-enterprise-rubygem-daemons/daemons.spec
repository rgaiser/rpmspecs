# Generated from daemons-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby /usr/local/bin/ruby
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname daemons
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A toolkit to create and control daemons in different ways
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.1.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://daemons.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Daemons provides an easy way to wrap existing ruby scripts (for example a
self-written server) 
to be run as a daemon and to be controlled by simple start/stop/restart
commands.
You can also call blocks as daemons and control them from the parent or just
daemonize the current
process.
Besides this basic functionality, daemons offers many advanced features like
exception 
backtracing and logging (in case your ruby script crashes) and monitoring and
automatic
restarting of your processes if they crash.


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
%doc %{geminstdir}/README
%doc %{geminstdir}/Releases
%doc %{geminstdir}/TODO
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 1.1.0-1
- Initial package

# Generated from mongrel-1.1.5.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname mongrel
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A small fast HTTP library and server that runs Rails, Camping, Nitro and Iowa apps
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.1.5
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://mongrel.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(gem_plugin) >= 0.2.3
Requires: ruby-enterprise-rubygem(daemons) >= 1.0.3
Requires: ruby-enterprise-rubygem(fastthread) >= 1.0.1
Requires: ruby-enterprise-rubygem(cgi_multipart_eof_fix) >= 2.4
BuildRequires: ruby-enterprise-rubygems
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
A small fast HTTP library and server that runs Rails, Camping, Nitro and Iowa
apps.

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
%{_bindir}/mongrel_rails
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/lib/mongrel/camping.rb
%doc %{geminstdir}/lib/mongrel/cgi.rb
%doc %{geminstdir}/lib/mongrel/command.rb
%doc %{geminstdir}/lib/mongrel/configurator.rb
%doc %{geminstdir}/lib/mongrel/const.rb
%doc %{geminstdir}/lib/mongrel/debug.rb
%doc %{geminstdir}/lib/mongrel/gems.rb
%doc %{geminstdir}/lib/mongrel/handlers.rb
%doc %{geminstdir}/lib/mongrel/header_out.rb
%doc %{geminstdir}/lib/mongrel/http_request.rb
%doc %{geminstdir}/lib/mongrel/http_response.rb
%doc %{geminstdir}/lib/mongrel/init.rb
%doc %{geminstdir}/lib/mongrel/rails.rb
%doc %{geminstdir}/lib/mongrel/stats.rb
%doc %{geminstdir}/lib/mongrel/tcphack.rb
%doc %{geminstdir}/lib/mongrel/uri_classifier.rb
%doc %{geminstdir}/lib/mongrel.rb
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 1.1.5-1
- Initial package

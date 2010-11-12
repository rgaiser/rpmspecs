# Generated from rake-0.8.7.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rake
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ruby based make-like utility
Name: ruby-enterprise-rubygem-%{gemname}
Version: 0.8.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rake.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
BuildRequires: ruby-enterprise-rubygems
BuildArch: noarch
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

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
%{_bindir}/rake
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/MIT-LICENSE
%doc %{geminstdir}/TODO
%doc %{geminstdir}/CHANGES
%doc %{geminstdir}/doc/command_line_usage.rdoc
%doc %{geminstdir}/doc/glossary.rdoc
%doc %{geminstdir}/doc/proto_rake.rdoc
%doc %{geminstdir}/doc/rakefile.rdoc
%doc %{geminstdir}/doc/rational.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.4.14.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.4.15.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.5.0.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.5.3.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.5.4.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.6.0.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.7.0.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.7.1.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.7.2.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.7.3.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.0.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.2.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.3.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.4.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.5.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.6.rdoc
%doc %{geminstdir}/doc/release_notes/rake-0.8.7.rdoc
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Thu Nov 11 2010 Roberto Gaiser <rgaiser@optimus.local> - 0.8.7-1
- Initial package

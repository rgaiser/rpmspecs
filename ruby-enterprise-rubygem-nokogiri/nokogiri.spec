# Generated from nokogiri-1.4.3.1.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname nokogiri
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser
Name: ruby-enterprise-rubygem-%{gemname}
Version: 1.4.3.1
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://nokogiri.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby-enterprise-rubygems
Requires: ruby-enterprise-rubygem(rubyforge) >= 2.0.4
Requires: ruby-enterprise-rubygem(racc) >= 0
Requires: ruby-enterprise-rubygem(rexical) >= 0
Requires: ruby-enterprise-rubygem(rake-compiler) >= 0
Requires: ruby-enterprise-rubygem(minitest) >= 1.6.0
Requires: ruby-enterprise-rubygem(hoe) >= 2.6.0
BuildRequires: ruby-enterprise-rubygems libxml2-devel libxslt-devel
Provides: ruby-enterprise-rubygem(%{gemname}) = %{version}

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.

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
%{_bindir}/nokogiri
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/CHANGELOG.ja.rdoc
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/README.ja.rdoc
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/ext/nokogiri/html_document.c
%doc %{geminstdir}/ext/nokogiri/html_element_description.c
%doc %{geminstdir}/ext/nokogiri/html_entity_lookup.c
%doc %{geminstdir}/ext/nokogiri/html_sax_parser_context.c
%doc %{geminstdir}/ext/nokogiri/nokogiri.c
%doc %{geminstdir}/ext/nokogiri/xml_attr.c
%doc %{geminstdir}/ext/nokogiri/xml_attribute_decl.c
%doc %{geminstdir}/ext/nokogiri/xml_cdata.c
%doc %{geminstdir}/ext/nokogiri/xml_comment.c
%doc %{geminstdir}/ext/nokogiri/xml_document.c
%doc %{geminstdir}/ext/nokogiri/xml_document_fragment.c
%doc %{geminstdir}/ext/nokogiri/xml_dtd.c
%doc %{geminstdir}/ext/nokogiri/xml_element_content.c
%doc %{geminstdir}/ext/nokogiri/xml_element_decl.c
%doc %{geminstdir}/ext/nokogiri/xml_encoding_handler.c
%doc %{geminstdir}/ext/nokogiri/xml_entity_decl.c
%doc %{geminstdir}/ext/nokogiri/xml_entity_reference.c
%doc %{geminstdir}/ext/nokogiri/xml_io.c
%doc %{geminstdir}/ext/nokogiri/xml_libxml2_hacks.c
%doc %{geminstdir}/ext/nokogiri/xml_namespace.c
%doc %{geminstdir}/ext/nokogiri/xml_node.c
%doc %{geminstdir}/ext/nokogiri/xml_node_set.c
%doc %{geminstdir}/ext/nokogiri/xml_processing_instruction.c
%doc %{geminstdir}/ext/nokogiri/xml_reader.c
%doc %{geminstdir}/ext/nokogiri/xml_relax_ng.c
%doc %{geminstdir}/ext/nokogiri/xml_sax_parser.c
%doc %{geminstdir}/ext/nokogiri/xml_sax_parser_context.c
%doc %{geminstdir}/ext/nokogiri/xml_sax_push_parser.c
%doc %{geminstdir}/ext/nokogiri/xml_schema.c
%doc %{geminstdir}/ext/nokogiri/xml_syntax_error.c
%doc %{geminstdir}/ext/nokogiri/xml_text.c
%doc %{geminstdir}/ext/nokogiri/xml_xpath_context.c
%doc %{geminstdir}/ext/nokogiri/xslt_stylesheet.c
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Sat Nov 13 2010 Roberto Gaiser <rgaiser@shrek.intranet> - 1.4.3.1-1
- Initial package

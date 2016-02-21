%global pkg_name apache-commons-lang3
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       lang
%global short_name      commons-%{base_name}3

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.1
Release:        9.10%{?dist}
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix}mvn(org.apache.commons:commons-parent:pom:) >= 26-7
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-assembly-plugin)
%if 0%{?rhel} <= 0
BuildRequires:  %{?scl_prefix}mvn(org.easymock:easymock)
%endif

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

With version of commons-lang 3.x, developers decided to change API and
therefore created differently named artifact and jar files. This is
the new version, while apache-commons-lang is the compatibility
package.

%package        javadoc
Summary:        API documentation for %{pkg_name}

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name} %{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build %{?rhel:-f}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 3.1-9.10
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 3.1-9.9
- maven33 rebuild

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.8
- Fix BR on apache-commons-parent

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 3.1-9.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 3.1-9.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.1-9
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-8
- Add BuildRequires on apache-commons-parent >= 26-7

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed May 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-6
- Build with xmvn
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.1-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Aug 27 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1-3
- Make easymock3 dependency conditional for Fedora

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 gil cattaneo <puntogil@libero.it> - 3.1-1
- update to 3.1

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.1-1
- Initial version of the package


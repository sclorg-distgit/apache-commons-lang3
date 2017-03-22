%global pkg_name apache-commons-lang3
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name       lang
%global short_name      commons-%{base_name}3

Name:           %{?scl_prefix}%{pkg_name}
Version:        3.4
Release:        2.3%{?dist}
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

# testParseSync() test fails on ARM and PPC64LE for unknown reason
Patch0:         fix-ppc64le-test-failure.patch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-io:commons-io)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.hamcrest:hamcrest-all)
%if 0%{?rhel} <= 0
BuildRequires:  %{?scl_prefix_maven}mvn(org.easymock:easymock)
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
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%patch0
%mvn_file : %{pkg_name} %{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build %{?rhel:-f}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt RELEASE-NOTES.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan  3 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4-2.3
- Build for rh-java-common
- Resolves: rhbz#1401051

* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 3.4-2.2
- Fix BR on maven-local & co.

* Mon Jan 18 2016 Michal Srb <msrb@redhat.com> - 3.4-2.1
- Prepare for SCL build

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Alexander Kurtakov <akurtako@redhat.com> 3.4-1
- Update to upstream 3.4.

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.2-3
- Fix build-requires on apache-commons-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.2-1
- Update to upstream version 3.3.2

* Thu Mar 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-2
- Disable test failing on PPC64LE

* Thu Mar 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-1
- Update to upstream version 3.3.1

* Tue Mar 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-1
- Update to upstream version 3.3

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.1-2
- Use Requires: java-headless rebuild (#1067528)

* Thu Jan  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-1
- Update to upstream version 3.2.1

* Thu Jan  2 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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

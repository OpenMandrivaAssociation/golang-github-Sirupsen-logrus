# http://github.com/sirupsen/logrus
%global goipath         github.com/sirupsen/logrus
Version:                1.1.1
%global old_goipath     github.com/Sirupsen/logrus

%gometa

Name:           golang-github-Sirupsen-logrus
Release:        1%{?dist}
Summary:        Structured logger for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
# Tests deps
BuildRequires: golang(github.com/stretchr/testify/assert)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall
%goinstall -i %{old_goipath} -o devel.file-list
pushd %{buildroot}/%{gopath}/src/%{old_goipath}/
sed -i 's/"github\.com\/sirupsen\/logrus/"github\.com\/Sirupsen\/logrus/g' \
        $(find . -name '*.go')
popd


%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
* Wed Oct 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- Release 1.1.1

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.4-5.gitd682213
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4.gitd682213
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.4-3.gitd682213
- Update to spec 3.0

* Fri Mar 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.4-2
- Autogenerate some parts using the new macros

* Tue Feb 20 2018 Kaushal <kshlmster@gmail.com> - 1.0.4-1
- Update to v1.0.4
- Use correct new source location s/Sirupsen/sirupsen/
- Provide both golang(github.com/sirupsen/logrus) and golang(github.com/Sirupsen/logrus)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Troy Dawson <tdawson@redhat.com> - 0.8.4-f10
- Cleanup spec file conditionals

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-6
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0.8.4-5
- Add hooks/bugsnag to provided packages
  related: #1246085

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-4
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.8.4-2
- Update spec file to spec-2.0
  related: #1246085

* Thu Jul 23 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0.8.4-1
- Bump to upstream 3cb248e9df77413d58a6330dde84236d04c197d5
  resolves: #1246085

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 jchaloup <jchaloup@redhat.com> - 0.6.4-1
- Bump to upstream 51fe59aca108dc5680109e7b2051cbdcfa5a253c
  related: #1158670

* Fri Jan 02 2015 jchaloup <jchaloup@redhat.com> - 0.6.2-1
- Update to 0.6.2
  related: #1158670

* Sun Nov 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.6.0-1
- Update to 0.6.0

* Thu Oct 30 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-2
- Resolves: rhbz#1158670 - initial package bug
- courtesy Jan Chaloupka <jchaloup@redhat.com>
- update dependencies
- add check

* Wed Oct 29 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.5.1-1
- Initial package

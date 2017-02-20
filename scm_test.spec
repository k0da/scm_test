#
# spec file for package scm_test
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           scm_test
Version:        0.1
Release:        0
License:        GPL
Summary:        service test 
Url:            http://github.com/k0da/scm_test
Group:          Packaging
Source:         %{name}-%{version}.tar.gz
BuildRequires:  filesystem
PreReq:         /usr/lib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
mkdir -p %{buildroot}/usr/lib/
install -m644 %{SOURCE0} %{buildroot}/usr/lib/

%install

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
/usr/lib/foo

%changelog


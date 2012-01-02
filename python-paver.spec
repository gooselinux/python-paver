%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define srcname Paver
Name: python-paver
Version: 1.0
Release: 4%{?dist}
Summary: Python-based build/distribution/deployment scripting tool

Group: Development/Languages
# The main paver code is licensed BSD
# The paver documentation includes jquery which is licensed MIT or GPLv2
License: BSD and (MIT or GPLv2) 
URL: http://www.blueskyonmars.com/projects/paver/
Source0: http://pypi.python.org/packages/source/P/%{srcname}/%{srcname}-%{version}.tar.gz
# This patch fixes a python-2.5ism so that paver can work with python-2.4.
# It's been accepted into upstream's tree 
Patch0: paver-python2.4.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools-devel
BuildRequires: python-sphinx
BuildRequires: python-nose

Requires:      python-devel
Requires:      python-setuptools

%description
Paver is a Python-based build/distribution/deployment scripting tool along the
lines of Make or Rake. What makes Paver unique is its integration with commonly
used Python libraries. Common tasks that were easy before remain easy. More
importantly, dealing with your applications specific needs and requirements is
now much easier.

* Build files are just Python
* One file with one syntax, pavement.py, knows how to manage your project
* File operations are unbelievably easy, thanks to the built-in version of
  Jason Orendorff’s path.py.
* Need to do something that takes 5 lines of code? It’ll only take 5 lines of
  code..
* Completely encompasses distutils and setuptools so that you can customize
  behavior as you need to.
* Wraps Sphinx for generating documentation, and adds utilities that make it
  easier to incorporate fully tested sample code.
* Wraps Subversion for working with code that is checked out.
* Wraps virtualenv to allow you to trivially create a bootstrap script that
  gets a virtual environment up and running. This is a great way to install
  packages into a contained environment.
* Can use all of these other libraries, but requires none of them
* Easily transition from setup.py without making your users learn about or
  even install Paver! (See the Getting Started Guide for an example).


%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1 -b .py2.4

# Note: This falls somewhere in between source and non-source.  It's a copy
# of the essential files from the library that's being packaged.  But it's
# zipped up.  For us, the paver command should find the uninstalled paver
# module in the directory so we might as well use it instead.
rm paver-minilib.zip

%build
%{__python} setup.py build

%check
%{__python} setup.py test

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%{_bindir}/*
%{python_sitelib}/*


%changelog
* Wed Jun 30 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-4
- fix license metdata
- add README.txt %%doc file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-2
- Patch for python-2.4 compatibility

* Tue Mar 24 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-1
- New upstream final.

* Thu Mar 19 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.1.b1
- New upstream beta.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-5
- Require python-setuptools as the paver app is a setuptools script.

* Mon Dec 15 2008 Luke Macken <lmacken@redhat.com> - 0.8.1-4
- Require python-devel.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8.1-3
- Rebuild for Python 2.6

* Sat Aug 9 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-2
- Run the unittests.

* Thu Aug 7 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-1
- Intial Fedora build.

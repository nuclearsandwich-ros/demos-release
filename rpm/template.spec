%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-demo-nodes-py
Version:        0.18.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS demo_nodes_py package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-example-interfaces
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-std-msgs
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-rolling-ament-copyright
BuildRequires:  ros-rolling-ament-flake8
BuildRequires:  ros-rolling-ament-pep257
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Python nodes which were previously in the ros2/examples repository but are now
just used for demo purposes.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Fri Dec 17 2021 Audrow Nash <audrow@openrobotics.org> - 0.18.0-1
- Autogenerated by Bloom

* Mon Oct 18 2021 Mabel Zhang <mabel@openrobotics.org> - 0.17.0-1
- Autogenerated by Bloom

* Wed Aug 11 2021 Mabel Zhang <mabel@openrobotics.org> - 0.16.0-1
- Autogenerated by Bloom

* Fri May 14 2021 Mabel Zhang <mabel@openrobotics.org> - 0.15.0-1
- Autogenerated by Bloom

* Mon Apr 26 2021 Mabel Zhang <mabel@openrobotics.org> - 0.14.2-1
- Autogenerated by Bloom

* Mon Apr 19 2021 Mabel Zhang <mabel@openrobotics.org> - 0.14.1-1
- Autogenerated by Bloom

* Tue Apr 06 2021 Mabel Zhang <mabel@openrobotics.org> - 0.14.0-1
- Autogenerated by Bloom

* Thu Mar 25 2021 Mabel Zhang <mabel@openrobotics.org> - 0.13.0-1
- Autogenerated by Bloom

* Thu Mar 18 2021 Mabel Zhang <mabel@openrobotics.org> - 0.12.1-1
- Autogenerated by Bloom

* Thu Mar 11 2021 Mabel Zhang <mabel@openrobotics.org> - 0.12.0-3
- Autogenerated by Bloom

* Thu Mar 11 2021 Mabel Zhang <mabel@openrobotics.org> - 0.12.0-2
- Autogenerated by Bloom

* Mon Mar 08 2021 Mabel Zhang <mabel@openrobotics.org> - 0.12.0-1
- Autogenerated by Bloom


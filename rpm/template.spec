%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-ur-description
Version:        2.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_description package

License:        BSD-3-Clause and Universal Robots A/S’ Terms and Conditions for Use of Graphical Documentation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-joint-state-publisher-gui
Requires:       ros-iron-launch
Requires:       ros-iron-launch-ros
Requires:       ros-iron-robot-state-publisher
Requires:       ros-iron-rviz2
Requires:       ros-iron-urdf
Requires:       ros-iron-xacro
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-pytest
BuildRequires:  ros-iron-launch-testing-ament-cmake
BuildRequires:  ros-iron-launch-testing-ros
BuildRequires:  ros-iron-xacro
BuildRequires:  urdfdom
%endif

%description
URDF description for Universal Robots

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
%license LICENSE
%license meshes/ur20/LICENSE.txt
/opt/ros/iron

%changelog
* Mon Apr 29 2024 Felix Exner <exner@fzi.de> - 2.3.0-1
- Autogenerated by Bloom

* Thu Apr 04 2024 Felix Exner <exner@fzi.de> - 2.1.4-1
- Autogenerated by Bloom

* Thu Dec 21 2023 Felix Exner <exner@fzi.de> - 2.1.3-1
- Autogenerated by Bloom

* Wed Dec 13 2023 Felix Exner <exner@fzi.de> - 2.1.2-1
- Autogenerated by Bloom

* Mon Sep 11 2023 Felix Exner <exner@fzi.de> - 2.1.1-1
- Autogenerated by Bloom

* Thu Jun 01 2023 Felix Exner <exner@fzi.de> - 2.1.0-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Felix Exner <exner@fzi.de> - 2.0.1-3
- Autogenerated by Bloom

* Wed Mar 22 2023 Felix Exner <exner@fzi.de> - 2.0.1-2
- Autogenerated by Bloom


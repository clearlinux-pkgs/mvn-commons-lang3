#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-lang3
Version  : 3.4
Release  : 7
URL      : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.jar
Source0  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.jar
Source1  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.jar
Source4  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.pom
Source5  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar
Source6  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.pom
Source7  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.pom
Source8  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar
Source9  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.pom
Source10  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.jar
Source11  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.pom
Source12  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.jar
Source13  : https://repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-lang3-data = %{version}-%{release}
Requires: mvn-commons-lang3-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-lang3 package.
Group: Data

%description data
data components for the mvn-commons-lang3 package.


%package license
Summary: license components for the mvn-commons-lang3 package.
Group: Default

%description license
license components for the mvn-commons-lang3 package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-lang3
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-lang3/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.2.1/commons-lang3-3.2.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.4/commons-lang3-3.4.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.7/commons-lang3-3.7.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-lang3/3.8.1/commons-lang3-3.8.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-lang3/LICENSE.txt

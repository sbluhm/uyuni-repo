%global debug_package %{nil}

Name:		terraform
Version:	0.13.5
Release:	1%{?dist}
Summary:	Tool for building infrastructure safely and efficiently

Group:		System/Management
License:	MPL-2.0
URL:		https://www.terraform.io/
Source0:	https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip

%description
Terraform is a tool for building, changing, and versioning infrastructure
safely and efficiently. Terraform can manage existing and popular service
providers as well as custom in-house solutions.


%prep
rm -Rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
unzip %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install terraform $RPM_BUILD_ROOT%{_bindir}


%files
%doc
%{_bindir}/%{name}


%changelog
* Sun Nov 08 2020 Stefan Bluhm <stefan.bluhm@clacee.eu>
- Initial version.

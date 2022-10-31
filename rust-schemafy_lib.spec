# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate schemafy_lib

Name:           rust-schemafy_lib
Version:        0.6.0
Release:        %autorelease
Summary:        Generates serializeable Rust types from a json schema

License:        MIT
URL:            https://crates.io/crates/schemafy_lib
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

# Upstream patches -- official upstream patches released by upstream since the
# ----------------    last release that are necessary for any reason:
Patch0001:      0001-docs-Add-a-README.md-and-LICENSE.patch

%global _description %{expand:
Generates serializeable Rust types from a json schema.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog

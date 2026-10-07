Name:           oobash
Version:        0.1.0
Release:        1%{?dist}
Summary:        Strict subset shell translating POSIX shell scripts into capability-audited openOODA AST.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobash
Source0:        oobash-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobash is a sovereign, capability-bounded COMPAT COMPILER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobash
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobash-uninstall

%files
/usr/bin/oobash
/usr/bin/oobash-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding

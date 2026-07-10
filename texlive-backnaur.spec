%global tl_name backnaur
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Typeset Backus Naur Form definitions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/backnaur
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package typesets Backus-Naur Form (BNF) definitions. It prints
formatted lists of productions, with numbers if required. It can also
print in-line BNF expressions using math mode.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/backnaur
%dir %{_datadir}/texmf-dist/source/latex/backnaur
%dir %{_datadir}/texmf-dist/tex/latex/backnaur
%doc %{_datadir}/texmf-dist/doc/latex/backnaur/README
%doc %{_datadir}/texmf-dist/doc/latex/backnaur/backnaur.pdf
%doc %{_datadir}/texmf-dist/source/latex/backnaur/backnaur.dtx
%doc %{_datadir}/texmf-dist/source/latex/backnaur/backnaur.ins
%{_datadir}/texmf-dist/tex/latex/backnaur/backnaur.sty

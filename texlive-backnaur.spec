Name:		texlive-backnaur
Version:	54080
Release:	1
Summary:	Typeset Backus Naur Form definitions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/backnaur
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.r54080.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.doc.r54080.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/backnaur.source.r54080.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package typesets Backus-Naur Form (BNF) definitions. It
creates aligned lists of productions, with numbers if required.
It can also print in-line BNF expressions using math mode.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/backnaur/backnaur.sty
%doc %{_texmfdistdir}/doc/latex/backnaur/README
%doc %{_texmfdistdir}/doc/latex/backnaur/backnaur.pdf
#- source
%doc %{_texmfdistdir}/source/latex/backnaur/backnaur.dtx
%doc %{_texmfdistdir}/source/latex/backnaur/backnaur.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

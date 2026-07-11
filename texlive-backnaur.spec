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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package typesets Backus-Naur Form (BNF) definitions. It prints
formatted lists of productions, with numbers if required. It can also
print in-line BNF expressions using math mode.


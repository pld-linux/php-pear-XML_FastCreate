%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	FastCreate
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - fast creation of valid XML with DTD control and translation options
Summary(pl):	%{_pearname} - szybkie tworzenie poprawnego XML-u ze sprawdzaniem DTD i opcjami dla t³umaczeñ
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	55ac0dee25243332e80cd4acedb846b4
URL:		http://pear.php.net/package/XML_FastCreate/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.2
Requires:	php-pear
Requires:	/usr/bin/php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(XML/Tree.*)' 'pear(XML/DTD.*)' 'pear(XML/Beautifier.*)' 'pear(XML/HTMLSax.*)'

%description
Key features of this package include:
- Easy way to make valid XML :
	$x->div(
	$x->h1("Example"),
	$x->p("Hello"),
	$x->p(array('class'=>'example'), "World !")
	)

- Option to report DTD errors in your XML :
Use internal tool or external program [ Require XML_DTD package ]

- Use output driver of your choice :
Text : return string
XML_Tree : return XML_Tree object [ Require XML_Tree package ]

- Translate option to quickly transform tags by anothers :
ex: Convert your XML to XHTML :
<news><title>Example</title></news>
to :
<div class="news"><h1>Example</h1></div>

- Include a PHP program to quickly transform HTML to FastCreate syntax.
[ Require XML_HTMLSax package ]

In PEAR status of this package is: %{_status}.

%description -l pl
Kluczowe mo¿liwo¶ci tego pakietu obejmuj±:
- prosty sposób tworzenia poprawnego XML-a:
	$x->div(
	$x->h1("Przyk³ad"),
	$x->p("Witaj"),
	$x->p(array('class'=>'example'), "¦wiecie!")
	)

- opcjê zg³aszania b³êdów DTD w XML-u:
u¿ycie wewnêtrznego narzêdzia lub zewnêtrznego programu (wymaga
pakietu XML_DTD)

- u¿ycie wybranego sterownika wyj¶ciowego:
Text : return string
XML_Tree : return XML_Tree object
(wymaga pakietu XML_Tree)

- opcjê t³umaczenia szybko przekszta³caj±c± znaczniki przez inne, np.
w celu przet³umaczenia XML-a na XHTML:
<news><title>Przyk³ad</title></news>
na:
<div class="news"><h1>Przyk³ad</h1></div>

- do³±czanie programu PHP do szybkiego przekszta³cania HTML-a do
sk³adni FastCreate (wymaga pakietu XML_HTMLSax).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{_bindir}
mv ./{%{php_pear_dir}/script/HTML2XFC.php,%{_bindir}/HTML2XFC}

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/tests/*,tests/%{_pearname}}

install -d ./%{php_pear_dir}/data/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/dtd/*,data/%{_pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
cp -a ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
%{php_pear_dir}/data/%{_pearname}

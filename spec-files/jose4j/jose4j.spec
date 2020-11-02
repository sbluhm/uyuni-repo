#
# spec file for package jose4j
#
# Copyright (c) 2016 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           jose4j
Version:        0.5.1
Release:        1.5.uyuni
Summary:        JWT implementation for Java
License:        Apache-2.0
Group:          Development/Languages/Java
Url:            https://bitbucket.org/b_c/jose4j
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  slf4j >= 1.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The jose.4.j library is a robust and easy to use open source implementation of
JSON Web Token (JWT) and the JOSE specification suite (JWS, JWE, and JWK).
It is written in Java and relies solely on the JCA APIs for cryptography.

%prep
%setup -q

%build
rm -rf src/test
find . -name '*.java' | xargs javac -encoding utf8 -source 1.7 -target 1.7 -cp $(build-classpath slf4j/all)
pushd src/main/java
jar cvf ../../../%{name}-%{version}.jar $(find . -name '*.class')
popd

%install
mkdir -p %{buildroot}%{_javadir}
install -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%defattr(-,root,root)
%doc LICENSE NOTICE.txt README.md
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%changelog
* Wed Aug  3 2016 dmacvicar@suse.de
- update to 0.5.1
- changes since 0.5.0
  * Addressed #65 so that the "class " prefix is not on the logger
    names of AlgorithmFactory
  * Addressed #63 with support for additional/arbitrary parameters
    in JWK
  * Addressed #64 by adding key_ops to JWK
  * Addressed #58 by having JwtClaims getAudience() and
    getStringListClaimValue(name) return an empty list rather than
    null when the claim isn’t present
- changes since 0.4.4
  * Addressed #37 with some fairly rudimentary but useful support
    for PEM encoded public keys
  * Addressed #54 by enabling HttpsJwks.getJsonWebKeys() to continue
    to use the existing cache when an exception is thrown from
    refresh().
    Default behavior is unchanged and
    setRetainCacheOnErrorDuration(...) must be called with a value
    larger than zero to get the new behavior.
  * #36 Added support for RFC 7638 JWK thumbprints
  * Addressed #35 by allowing the caller of various JOSE and JWT
    functionality to specify a particular JCA provider by name for
    cryptographic operations
  * Addressed #44 by providing a generic callback to JwtConsumer
    to customize each JWS/JWE
  * Addressed #43 now supports the 'crit' header
  * Fix ClassCastException with AndroidKeyStoreRSAPrivateKey on
    Android 6.0 Marshmallow
  * Fix #46 by using the original encoded payload in signature
    verification rather than a re-encoding of the payload
  * Addressed #48 by providing a method for getting a JWS with
    detached content
  * Fix #38 by not logging secrets and other info from
    ConcatKeyDerivationFunction
  * Fix #41 allowing users to specify arbitrary NumericDate
    values
  * Fix #39 - no more NPE by conditionally avoiding key length
    checks when raw secret key isn’t available because of
    non-extractable key data due to PKCS11/HSM provider
- add %%defattr
* Wed Nov 18 2015 ro@suse.de
- fix group entry in specfile
* Fri Oct 23 2015 dmacvicar@suse.de
- initial version for 0.4.4

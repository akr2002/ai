# Taken from https://flyx.org/nix-flakes-latex/
{
  description = "AI worksheet";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    with flake-utils.lib;
      eachSystem allSystems (system: let
        pkgs = nixpkgs.legacyPackages.${system};
        tex = pkgs.texlive.combine {
          inherit (pkgs.texlive) scheme-basic pgf nicematrix latex-bin latexmk titlesec booktabs listings sectsty;
        };
      in rec {
        packages = {
          document = pkgs.stdenvNoCC.mkDerivation rec {
            name = "latex-demo-document";
            src = self;
            buildInputs = [pkgs.coreutils tex pkgs.pandoc pkgs.texliveFull pkgs.tetex];
            phases = ["unpackPhase" "buildPhase" "installPhase"];
            buildPhase = ''
              export PATH="${pkgs.lib.makeBinPath buildInputs}";
                #pandoc rpa.md -s -o rpa.tex --pdf-engine=xelatex
                mkdir -p .cache/texmf-var
                env TEXMFHOME=.cache TEXMFVAR=.cache/texmf-var \
                  latexmk -f -interaction=nonstopmode -pdf -lualatex \
                  e1.tex
            '';
            installPhase = ''
              mkdir -p $out
              cp e1.pdf $out/
            '';
          };
        };
        defaultPackage = packages.document;
      });
}

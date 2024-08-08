  {
    description = "python";
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
    neve = {
      url = "github:redyf/Neve";
    };
  };
  outputs = { nixpkgs, flake-utils, neve, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
    in rec {
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python3.withPackages(ps: with ps; [
            cairosvg
            ipython
            jupyter
            jupyter-client
            jupytext
            numpy
            pandas
            pynvim
          ]))
        ];
        shellHook = "";
      };
    }
  );
}

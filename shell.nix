{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	packages = with pkgs; [
		git
		python311
		pkgs.pdm
	];
}

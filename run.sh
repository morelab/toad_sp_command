#!/bin/sh

ORIGIN_DIRECTORTY=$(pwd)
BASEDIR=$(dirname "$0")
{
  cd "$BASEDIR"
  python -m toad_sp_controller.main
} || {
  :
}
cd "$ORIGIN_DIRECTORTY"
import sys                                  as _sys

from click.testing                          import CliRunner

from shelah_cli.cli.ela_cli                 import ela_cli

runner = CliRunner()

class Test_Ela_CLI:

    def test_get_theories(self):
        response = runner.invoke(ela_cli, ["get", "theories"])
        assert response.exit_code == 0
        #assert "Contact test-user added!" in response.output
        #assert "{'mobile': '0'}" in response.output



if __name__ == "__main__":
    # execute only if run as a script
    def main(args):
        T = Test_Ela_CLI()
        #T.setUp()
        what_to_do = args[1]
        if what_to_do=="get_theories":
            T.test_get_theories()


    main(_sys.argv)
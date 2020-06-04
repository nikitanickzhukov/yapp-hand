#include <boost/format.hpp>
#include <boost/program_options.hpp>
#include <pokerstove/peval/CardSet.h>
#include <pokerstove/peval/PokerHandEvaluator.h>
#include <iostream>
#include <vector>

using namespace pokerstove;
namespace po = boost::program_options;
using namespace std;

int main(int argc, char** argv)
{
    po::options_description desc("ps-id, a poker hand identifier\n");

    desc.add_options()
        ("help,?",  "produce help message")
        ("game,g",  po::value<string>()->default_value("h"),    "game to use for identification")
        ("board,b", po::value<string>(),                        "community cards for he/o/o8")
        ("hand,h",  po::value<string>(),                "a hand for identification")
        ("quiet,q", "produces no output");

    // make hand a positional argument
    po::positional_options_description p;
    p.add("hand", -1);

    po::variables_map vm;
    po::store(po::command_line_parser(argc, argv)
                  .style(po::command_line_style::unix_style)
                  .options(desc)
                  .positional(p)
                  .run(),
              vm);
    po::notify(vm);

    // check for help
    if (vm.count("help") || argc == 1)
    {
        cout << desc << endl;
        return 1;
    }

    // extract the options
    string game = vm["game"].as<string>();
    string board = vm.count("board") ? vm["board"].as<string>() : "";
    string hand = vm["hand"].as<string>();

    bool quiet = vm.count("quiet") > 0;

    CardSet pit = CardSet(hand);
    CardSet bit = CardSet(board);

    auto evaluator = PokerHandEvaluator::alloc(game);
    PokerHandEvaluation eval = evaluator->evaluate(pit, bit);

    if (!quiet)
    {
        cout << eval.high().str() << endl;
        cout << eval.high().code() << endl;
        if (eval.low().code())
        {
            cout << eval.low().str() << endl;
            cout << eval.low().code() << endl;
        }
    }
}

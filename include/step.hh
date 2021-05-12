#include "message.hh"
#include <iostream>
#include <sstream>
namespace step
{
	#define STEP
	int debug_step = 0;
	void step(int step_number, std::string message, std::string type){
		debug_step += step_number;
		int step = step_number;
		std::stringstream sstm;
		sstm << "Step " << step_number << ":\n" << message << std::endl;
		std::string result = sstm.str();
		if (type == "error") {
			message::printerror(result);
		};
		if (type == "success") {
			message::printsuccess(result);
		};
		if (type == "warning") {
			message::printwarning(result);
		};
		if (type == "info") {
			message::printinfo(result);
		};
	};
}; // namespace step

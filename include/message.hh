#pragma once
#include <iostream>
#include "./color.hh"
namespace message
{
	void printreset()
	{
		std::cout << RESET << std::endl;
	}

	void printwarning(std::string message)
	{
		std::cout << BOLDYELLOW << message;
		printreset();
	}
	void printerror(std::string message)
	{
		std::cout << BOLDRED << message;
		printreset();
	}
	void printinfo(std::string message)
	{
		std::cout << BOLDBLUE << message;
		printreset();
	}
	void printsuccess(std::string message)
	{
		std::cout << BOLDGREEN << message;
		printreset();
	}
} // namespace message

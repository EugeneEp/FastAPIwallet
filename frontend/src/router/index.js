import Vue from 'vue';
import Router from 'vue-router';
import Users from '@/components/Products'
import Index from '@/components/Index'
import About from '@/components/about'
import Business from '@/components/business'
import Capabilities from '@/components/capabilities'
import Contacts from '@/components/contacts'
import Events from '@/components/events'
import Gaming from '@/components/gaming'
import Stream from '@/components/stream'
import StartBusiness from '@/components/startBusiness'
import userLogout from '@/components/userLogout'
import Wallet from '@/components/wallet/wallet.vue'
import Profile from '@/components/wallet/profile.vue'
import Charge from '@/components/wallet/charge.vue'
import Donate from '@/components/wallet/donate.vue'
import Partner from '@/components/wallet/partner.vue'
import Transfer from '@/components/wallet/transfer.vue'
import Moneybank from '@/components/wallet/moneybank.vue'

Vue.use(Router);

export default new Router({
	routes: [
		{
			path: '/wallet/partner',
			name: 'Partner',
			component: Partner,
		},
		{
			path: '/wallet/transfer',
			name: 'Transfer',
			component: Transfer,
		},
		{
			path: '/wallet/moneybank',
			name: 'Moneybank',
			component: Moneybank,
		},
		{
			path: '/wallet/donate',
			name: 'Donate',
			component: Donate,
		},
		{
			path: '/wallet/charge',
			name: 'Charge',
			component: Charge,
		},
		{
			path: '/wallet/profile',
			name: 'Profile',
			component: Profile,
		},
		{
			path: '/wallet',
			name: 'Wallet',
			component: Wallet,
		},
	    {
	    	path: '/products',
	    	name: 'Products',
	    	component: Users,
	    },
	    {
	    	path: '/',
	    	name: 'Index',
	    	component: Index
	    },
	    {
	    	path: '/start-business/info',
	    	name: 'StartBusiness',
	    	component: StartBusiness
	    },
	    {
	    	path: '/events/info',
	    	name: 'Events',
	    	component: Events
	    },
	    {
	    	path: '/capabilities/info',
	    	name: 'Capabilities',
	    	component: Capabilities
	    },
	    {
	    	path: '/gaming/info',
	    	name: 'Gaming',
	    	component: Gaming
	    },
	    {
	    	path: '/business/info',
	    	name: 'Business',
	    	component: Business
	    },
	    {
	    	path: '/contacts/info',
	    	name: 'Contacts',
	    	component: Contacts
	    },
	    {
	    	path: '/about/info',
	    	name: 'About',
	    	component: About
	    },
	    {
	    	path: '/stream/info',
	    	name: 'Stream',
	    	component: Stream
	    },
	    {
	    	path: '/userLogout',
	    	name: 'userLogout',
	    	component: userLogout
	    }
	],
	mode: 'history',
});
